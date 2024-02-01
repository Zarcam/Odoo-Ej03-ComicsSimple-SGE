from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BaseArchive(models.AbstractModel):    
    _name = 'base.archive'
    _description = 'Fichero abstracto'
    
    activo = fields.Boolean(default=True)
            
    def archivar(self):        
        for record in self:            
            record.activo = not record.activo


class BibliotecaComic(models.Model):
    
    _name = 'biblioteca.comic'    
    _inherit = ['base.archive']

    _description = 'Comic de biblioteca'
    
    _order = 'fecha_publicacion desc, nombre'
             
    _rec_name = 'nombre'    
    nombre = fields.Char('Titulo', required=True, index=True)    
    estado = fields.Selection(
        [('borrador', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        'Estado', default="borrador")    
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)    
    portada = fields.Binary('Portada Comic')
    
    fecha_publicacion = fields.Date('Fecha publicación')
    
    precio = fields.Float('Precio')    
    paginas = fields.Integer('Numero de páginas',                
        groups='base.group_user',        
        estados={'perdido': [('readonly', True)]},        
        help='Total numero de paginas',                        
        company_dependent=False)
     
    valoracion_lector = fields.Float(
        'Valoración media lectores',
    digits=(14, 4),  
    )            
    autor_ids = fields.Many2many('res.partner', string='Autores')
        
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El titulo Comic debe ser único.'),
        ('positive_page', 'CHECK(paginas>0)', 'El comic debe tener al menos una página')
    ]
                
    @api.constrains('fecha_publicacion')
    def _check_release_date(self):        
        for record in self:                        
            if record.fecha_publicacion and record.fecha_publicacion > fields.Date.today():                
                raise models.ValidationError('La fecha de lanzamiento debe ser anterior a la actual')