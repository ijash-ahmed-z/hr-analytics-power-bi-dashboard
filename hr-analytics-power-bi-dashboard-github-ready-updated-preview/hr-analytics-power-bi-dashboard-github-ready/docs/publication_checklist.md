# Publication checklist

Before making the repository public, review the following items in Power BI Desktop:

1. **Validate the Power Query row-removal rule.** The current query sorts by `Years With Current Manager` and then removes the first 57 rows. Confirm that this exclusion is intentional and document the business rule. If it is not intentional, remove the step and refresh the report.
2. **Replace the local CSV path.** The PBIX points to a local Windows file path. Use **Data source settings** or a Power Query parameter so another user can refresh the report.
3. **Confirm dataset redistribution rights.** This package does not publish employee-level source data. Only aggregated outputs are included.
4. **Export an original dashboard screenshot.** Open the report at 100% zoom and replace `assets/dashboard-preview.png` if you want the README to show the exact Power BI rendering.
5. **Check labels.** The source model contains the column name `Empoyee ID`; correct it to `Employee ID` during the next report revision.
