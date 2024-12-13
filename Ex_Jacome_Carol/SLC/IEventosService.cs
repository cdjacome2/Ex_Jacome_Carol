using Entities;
using System.Collections.Generic;

namespace SLC
{
    public interface IEventosService
    {
        Evento CreateEvento(Evento evento);
        bool DeleteEvento(int id);
        List<Evento> GetAllEventos();
        Evento GetEventoById(int id);
        bool UpdateEvento(Evento evento);
    }
}
