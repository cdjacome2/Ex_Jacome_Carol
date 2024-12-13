using System.Collections.Generic;
using BLL;
using Entities;

namespace SOAPService
{
    public class Service1 : IService1
    {
        private readonly EventosLogic _eventosLogic;

        public Service1()
        {
            _eventosLogic = new EventosLogic();
        }

        public List<Evento> GetAllEventos()
        {
            return _eventosLogic.GetAllEventos();
        }

        public Evento GetEventoById(int id)
        {
            return _eventosLogic.GetEventoById(id);
        }

        public bool CreateEvento(Evento evento)
        {
            return _eventosLogic.CreateEvento(evento);
        }

        public bool UpdateEvento(Evento evento)
        {
            return _eventosLogic.UpdateEvento(evento);
        }

        public bool DeleteEvento(int id)
        {
            return _eventosLogic.DeleteEvento(id);
        }
    }
}
