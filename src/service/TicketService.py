import logging
from re import I
from pojo.Ticket import Ticket
from repository.AreaRepository import AreaRepository
from repository.CriticidadRepository import CriticidadRepository
from repository.EstadoTicketRepository import EstadoTicketRepository
from repository.TicketRepository import TicketRepository
from repository.TipoTicketRepository import TipoTicketRepository


class TicketService:
    
    def __init__(self):
        self.ticketRepo = TicketRepository._ticketRepository
        self.criticidadRepo = CriticidadRepository._criticidadRepository
        self.areaRepo = AreaRepository._areaRepository
        self.tipoTicketRepo = TipoTicketRepository._tipoTicketRepository
        self.estadoTicket = EstadoTicketRepository._estadoTicketRepository
        
        
    def guardarTicket(self,ticket):
        return self.ticketRepo.guardarTicket(ticket)
    def actualizarTicket(self,ticket):
        return self.ticketRepo.actualizarTicket(ticket)
    
    def obtenerCriticidades(self):
        return self.criticidadRepo.obtenerCriticidades()
    
    def obenerAreas(self):
        return self.areaRepo.obtenerAreas();
    
    
    def obtenerTiposTickets(self):
        return self.tipoTicketRepo.obtenerTipoTickets()
    
    def obtenerTicketsAsignados(self,idUsuario):
        tickets =self.ticketRepo.obtenerTicketsUsuario(idUsuario)
        return tickets
    def obtenerEstadosTicket(self):
        return self.estadoTicket.obtenerEstadosTicket()
    def guardarArea(self,areaEntity):
        return self.areaRepo.guardarArea(areaEntity)   
    def obtenerAreas(self):
        return self.areaRepo.obtenerAreas()
    
    def validarRelacionArea(self, idAreaAValidar):
        try:
            
            cantidad = self.ticketRepo.obtenerTicketsRelacionados(idAreaAValidar)
            if cantidad <=0:
                return True
            else:
                return False
        except Exception as error:
            logging.error("ocurio un error al validar las areas en la tabla de tickets, se retornara True")
            logging.error(error)
            return True
    def eliminarArea(self, idAreaEliminar):
        return self.areaRepo.eliminarArea(idAreaEliminar)       
    @staticmethod
    def build():
        TicketService._ticketService = TicketService()
             
    