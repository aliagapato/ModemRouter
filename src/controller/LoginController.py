
import logging
from entity.UsuarioEntity import UsuarioEntity
from service.UsuarioService import UsuarioService


class LoginController:
    
    def __init__(self) :
        self.usuarioService = UsuarioService._usuarioService
        pass
    
    def login(self,user, password ):
        try:
            logging.info("se inicia login de usuario")
            usuario =  self.usuarioService.validarusuario(user,password)
            logging.info("se termina login de usuario")
            return usuario
        except Exception as error:
            logging.error(error)
            return UsuarioEntity()
    @staticmethod
    def build():
        UsuarioService._usuarioService = UsuarioService()