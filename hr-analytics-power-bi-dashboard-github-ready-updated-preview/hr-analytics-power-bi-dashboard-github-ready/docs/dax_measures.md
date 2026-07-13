# DAX measures

The following measures were extracted from the submitted PBIX model.

## Total Employees

```DAX
sum(HR_Analytics[Employee Count])
```

## Employees Left

```DAX
CALCULATE(
    COUNTROWS('HR_Analytics'),
    'HR_Analytics'[Attrition] = "Yes"
)
```

## Average Monthly Income

```DAX
AVERAGE(HR_Analytics[Monthly Income])
```

## Attrition Rate

```DAX
([Employees Left]/[Total Employees])
```
