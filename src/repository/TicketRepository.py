import logging
from config.Config import Config
from entity.AreaEntity import AreaEntity
from entity.TicketEntity import TicketEntity
from pojo.Ticket import Ticket


class TicketRepository:
    
    def __init__(self):
        self._dbConn = Config._dbConnection
        
    def obtenerTickets(self):
        try:
            SQL = "SELECT * FROM tma.ticket"
            cursor =  self._dbConn.cursor()
        
            cursor.execute(SQL)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(TicketEntity.creaTicketEntity(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
        
        
        
    def guardarTicket(self,ticket):
        try:
            cursor =  self._dbConn.cursor()
            SQL = """
            INSERT INTO
                `tma`.`ticket` (
                    `nombre_cliente`,
                    `rut_cliente`,
                    `telefono`,
                    `correo_electronico`,
                    `detalle`,
                    `observacion`,
                    `id_estado`,
                    `fecha_creacion`,
                    `id_usuario_creacion`,
                    `id_usuario_derivado`,
                    `id_criticidad`,
                    `id_area`,
                    `id_tipo_ticket`
                )
            VALUES
                (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
                );

            """
            val = (
                ticket.nombreCliente,
                ticket.rutCliente,
                ticket.telefono,
                ticket.correoElectronico,
                ticket.detalle,
                ticket.observacion,
                ticket.idEstado,
                ticket.fechaCreacion,
                ticket.idUsuarioCreacion,
                ticket.idUsuarioDerivado,
                ticket.idCriticidad,
                ticket.idArea,
                ticket.idTipoTicket,
               
            )
            
            cursor.execute(SQL, val)
            self._dbConn.commit()  
        except Exception as error:
            logging.error("ocurrio un error al guardar el ticket en la base de datos")
            logging.error(error)
            
    def actualizarTicket (self, ticket):
        try:
            cursor =  self._dbConn.cursor()
            SQL = """
            UPDATE
                `tma`.`ticket`
            SET
                `nombre_cliente` = %s,
                `rut_cliente` = %s,
                `telefono` =%s,
                `correo_electronico`=%s,
                `detalle` = %s,
                `observacion` = %s,
                `id_estado` = %s,
                `fecha_creacion` = %s,
                `id_usuario_creacion` = %s,
                `id_usuario_derivado` = %s,
                `id_criticidad` = %s,
                `id_area` = %s,
                `id_tipo_ticket` = %s
            WHERE
                `id_ticket` = %s

            """
            val = (
                ticket.nombreCliente,
                ticket.rutCliente,
                ticket.telefono,
                ticket.correoElectronico,
                ticket.detalle,
                ticket.observacion,
                ticket.idEstado,
                ticket.fechaCreacion,
                ticket.idUsuarioCreacion,
                ticket.idUsuarioDerivado,
                ticket.idCriticidad,
                ticket.idArea,
                ticket.idTipoTicket,
                ticket.id
               
            )
            
            cursor.execute(SQL, val)
            self._dbConn.commit()  
        except Exception as error:
            logging.error("ocurrio un error al guardar el ticket en la base de datos")
            logging.error(error)
    def obtenerTicketsRelacionados(self, idAreaRelacionado):
        try:
            SQL = "SELECT count(*) FROM tma.ticket where id_area =%s"
            cursor =  self._dbConn.cursor()
            val = (idAreaRelacionado,)
            cursor.execute(SQL,val)

            result= cursor.fetchall()
            cursor.close()  
            
            return int(result[0][0])
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def obtenerTicketsUsuario(self,idUsuario):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        u2.id_usuario = %s"""
            cursor =  self._dbConn.cursor()
            val = (idUsuario,)
            cursor.execute(SQL,val)

            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def buscarTicketsPorFechaCreacion(self,fechaCreacion ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                     DATE_FORMAT(t.fecha_creacion,'%Y-%b-%d')    = DATE_FORMAT(%s,'%Y-%b-%d')"""
            cursor =  self._dbConn.cursor()
            val = (fechaCreacion,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def buscarTicketPorCriticidad(self,idCriticidad ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        t.id_criticidad    = %s"""
            cursor =  self._dbConn.cursor()
            val = (idCriticidad,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def buscarTicketPorTipoTicket(self,idTipoTicket ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        t.id_tipo_ticket    = %s"""
            cursor =  self._dbConn.cursor()
            val = (idTipoTicket,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def buscarTicketsPorUsuarioCreacion(self,idUsuario ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        t.id_usuario_creacion    = %s"""
            cursor =  self._dbConn.cursor()
            val = (idUsuario,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    def buscarTicketsPorUsuarioCierre(self,idUsuario ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        t.id_usuario_derivado    = %s and t.id_estado = 2"""
            cursor =  self._dbConn.cursor()
            val = (idUsuario,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception

    def buscarTicketsPorArea(self,idArea ):
        try:
            SQL = """ select
                        t.id_ticket,
                        t.nombre_cliente,
                        t.rut_cliente,
                        t.telefono,
                        t.correo_electronico,
                        t.detalle,
                        t.observacion,
                        t.id_estado,
                        et.nom_estado_ticket,
                        t.fecha_creacion,
                        t.id_usuario_creacion,
                        u1.nombre_usuario,
                        t.id_usuario_derivado,
                        u2.nombre_usuario,
                        t.id_criticidad,
                        c.nom_criticidad,
                        t.id_area,
                        a.nom_area,
                        t.id_tipo_ticket,
                        tt.nom_tipo_ticket
                    from
                        ticket as t
                        join estado_ticket as et on t.id_estado = et.id_estado_ticket
                        join usuario as u1 on t.id_usuario_creacion = u1.id_usuario
                        join usuario as u2 on t.id_usuario_derivado = u2.id_usuario
                        join criticidad as c on t.id_criticidad = c.id_criticidad
                        join area as a on t.id_area = a.id_area
                        join tipo_ticket as tt on t.id_tipo_ticket = tt.id_tipo_ticket
                    where
                        t.id_area    = %s"""
            cursor =  self._dbConn.cursor()
            val = (idArea,)
            cursor.execute(SQL,val)
            logging.info(cursor)
            result= cursor.fetchall()
            cursor.close()  
            
            res = []
            for item in result:
                res.append(Ticket.creaTicket(item))
            return res
        except Exception as error:
            logging.error("ocurrio un error al intentar obtener los tickets")
            logging.error(error)
            raise Exception
    @staticmethod
    def build():
        TicketRepository._ticketRepository = TicketRepository()    
