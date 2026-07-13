from pathlib import Path
import pandas as pd
from pbixray import PBIXRay

PBIX_PATH = Path("dashboard/HR_Analytics_Dashboard.pbix")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

with PBIXRay(PBIX_PATH) as model:
    df = model.get_table("HR_Analytics")

left_mask = df["Attrition"].eq("Yes")
summary = pd.DataFrame({
    "Metric": ["Total Employees", "Employees Left", "Attrition Rate", "Average Monthly Income"],
    "Value": [
        int(df["Employee Count"].sum()),
        int(left_mask.sum()),
        float(left_mask.mean()),
        float(df["Monthly Income"].mean()),
    ],
})
summary.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

for column, filename in {
    "Age Group": "attrition_by_age_group.csv",
    "Department": "attrition_by_department.csv",
    "Education Field": "attrition_by_education_field.csv",
    "Salary Slab": "attrition_by_salary_slab.csv",
    "Years At Company": "attrition_by_years_at_company.csv",
}.items():
    result = df.groupby(column).agg(
        Employees=("Attrition", "size"),
        Employees_Left=("Attrition", lambda s: int(s.eq("Yes").sum())),
    ).reset_index()
    result["Attrition_Rate"] = result["Employees_Left"] / result["Employees"]
    result.to_csv(OUTPUT_DIR / filename, index=False)

print(f"Exported summaries to {OUTPUT_DIR.resolve()}")
