using System;
using System.Collections.Generic;
using System.Linq;
using DAL;
using Entities;

namespace BLL
{
    public class EventosLogic
    {
        private readonly DB_EventosEntities _context;

        public EventosLogic()
        {
            _context = new DB_EventosEntities();
        }

        public List<Evento> GetAllEventos()
        {
            return _context.Eventos.Select(e => new Evento
            {
                EventoID = e.EventoID,
                Nombre = e.Nombre,
                Lugar = e.Lugar,
                FechaInicio = e.FechaInicio,
                FechaFin = e.FechaFin,
                Descripcion = e.Descripcion
            }).ToList();
        }

        public Evento GetEventoById(int id)
        {
            var evento = _context.Eventos.FirstOrDefault(e => e.EventoID == id);
            if (evento == null) return null;

            return new Evento
            {
                EventoID = evento.EventoID,
                Nombre = evento.Nombre,
                Lugar = evento.Lugar,
                FechaInicio = evento.FechaInicio,
                FechaFin = evento.FechaFin,
                Descripcion = evento.Descripcion
            };
        }

        public bool CreateEvento(Evento nuevoEvento)
        {
            try
            {
                _context.Eventos.Add(new DAL.Eventos
                {
                    Nombre = nuevoEvento.Nombre,
                    Lugar = nuevoEvento.Lugar,
                    FechaInicio = nuevoEvento.FechaInicio,
                    FechaFin = nuevoEvento.FechaFin,
                    Descripcion = nuevoEvento.Descripcion
                });
                _context.SaveChanges();
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public bool UpdateEvento(Evento evento)
        {
            try
            {
                var existingEvento = _context.Eventos.FirstOrDefault(e => e.EventoID == evento.EventoID);
                if (existingEvento == null) return false;

                existingEvento.Nombre = evento.Nombre;
                existingEvento.Lugar = evento.Lugar;
                existingEvento.FechaInicio = evento.FechaInicio;
                existingEvento.FechaFin = evento.FechaFin;
                existingEvento.Descripcion = evento.Descripcion;

                _context.SaveChanges();
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public bool DeleteEvento(int id)
        {
            try
            {
                var evento = _context.Eventos.FirstOrDefault(e => e.EventoID == id);
                if (evento == null) return false;

                _context.Eventos.Remove(evento);
                _context.SaveChanges();
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
