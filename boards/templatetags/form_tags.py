# -*- coding:utf-8 -*-
###
# Created Date: Wednesday, June 27th 2018, 4:53:15 pm
# Author: John
# Email: zhouqiang847@gmail.com
###

from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':  # 解决密码输入框样式问题
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)
