# Mini-Project: Using Custom Filters

The attached starter project simply displays a list of ToDo items from a model using a custom filer to display human-friendly date descriptions.

* Setup/use the Django admin module to add at least 5 ToDo items with dates both in the past and the future
* Verify that all items display properly using the initial custom filter. The starter custom filter can be found in ```templatetags``` and applies the following rules:

- If ToDo item due date is current date, display 'TODAY'
- If ToDo item due date has past, display the number of days overdue
- If ToDo item due date is in 1 day, display 'TOMORROW'
- If ToDo item due date is in future, display number of days in future item is due

### Your challenge is the following
- Create a custom filter to apply a CSS border that will highlight the ToDo items with a border depending on if their due date is less than a day away (```#FF0000```), less than or equal to 3 days away (```#FF7400```), otherwise set the border to ```#00CC00``` (green)

### Tips:

- Register your new filter in ```app_filters.py```  using ```@register.filter(name='get_due_date_color')```

- You will have to use the 'pipe' operator to pass your output into your filter. Using an inline style will be the easiest way:

```<div style='border: 2px solid {{todo.due_date|get_due_date_color}};'>{{whatever todo item}}</div>```

- You should not have to alter any code other than the ```index.html``` template and the ```app_filters``` custom template file
