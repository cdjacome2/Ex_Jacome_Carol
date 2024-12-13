using System.Collections.Generic;
using System.ServiceModel;
using Entities;

namespace SOAPService
{
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        List<Evento> GetAllEventos();

        [OperationContract]
        Evento GetEventoById(int id);

        [OperationContract]
        bool CreateEvento(Evento evento);

        [OperationContract]
        bool UpdateEvento(Evento evento);

        [OperationContract]
        bool DeleteEvento(int id);
    }
}
