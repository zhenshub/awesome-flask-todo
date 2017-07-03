from wtforms import Form, DateField, StringField, IntegerField, validators


class AddTodoForm(Form):
    content = StringField('content', [validators.length(min=3, max=20)])
    time = DateField('date', [validators.data_required()])
    status = IntegerField('status', [validators.number_range(max=1, min=0)])

