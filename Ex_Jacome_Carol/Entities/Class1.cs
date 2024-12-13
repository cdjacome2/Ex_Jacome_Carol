using System;

namespace Entities
{
    public class Evento
    {
        public int EventoID { get; set; }
        public string Nombre { get; set; }
        public string Lugar { get; set; }
        public DateTime FechaInicio { get; set; }
        public DateTime? FechaFin { get; set; } 
        public string Descripcion { get; set; }
    }
}
