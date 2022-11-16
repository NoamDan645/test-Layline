# -*- coding: utf-8 -*-
from odoo import fields, models


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name')
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
    
class ProductCategory(models.Model):
    _name = 'supermarket.product.category'
    _description = 'Product Category'

    name = fields.Char(string='Name')

class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'

    name = fields.Char('Name')
    product_category_id = fields.Many2one(comodel_name='supermarket.product.category', string='Product Category')
    price = fields.Float('Price')

class Cart(models.Model):
    _name = 'supermarket.cart'
    _description = 'Cart'

    customer_id = fields.Many2one(comodel_name='supermarket.customer', string='Customer', required=True)
    date = fields.Date(string='Date')