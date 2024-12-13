using System;
using System.Collections.Generic;
using BLL;
using Entities;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            var eventosLogic = new EventosLogic();

            Console.WriteLine("===== Pruebas CRUD para Eventos =====");

            // Crear un nuevo evento
            Console.WriteLine("\nCreando un nuevo evento...");
            var nuevoEvento = new Evento
            {
                Nombre = "Conferencia Tech 2024",
                Lugar = "Centro de Convenciones",
                FechaInicio = new DateTime(2024, 12, 15, 9, 0, 0),
                FechaFin = new DateTime(2024, 12, 15, 17, 0, 0),
                Descripcion = "Evento de tecnología sobre inteligencia artificial y software."
            };
            if (eventosLogic.CreateEvento(nuevoEvento))
            {
                Console.WriteLine("Evento creado con éxito.");
            }
            else
            {
                Console.WriteLine("Error al crear el evento.");
            }

            // Obtener todos los eventos
            Console.WriteLine("\nObteniendo todos los eventos...");
            var eventos = eventosLogic.GetAllEventos();
            foreach (var evento in eventos)
            {
                Console.WriteLine($"ID: {evento.EventoID}, Nombre: {evento.Nombre}, Lugar: {evento.Lugar}, FechaInicio: {evento.FechaInicio.ToShortDateString()}, FechaFin: {evento.FechaFin?.ToShortDateString()}, Descripción: {evento.Descripcion}");
            }

            // Actualizar un evento
            Console.WriteLine("\nActualizando un evento...");
            if (eventos.Count > 0)
            {
                var eventoParaActualizar = eventos[0];
                eventoParaActualizar.Nombre = "Conferencia Tech 2024 - Actualizado";
                eventoParaActualizar.Lugar = "Auditorio Principal";
                if (eventosLogic.UpdateEvento(eventoParaActualizar))
                {
                    Console.WriteLine("Evento actualizado con éxito.");
                }
                else
                {
                    Console.WriteLine("Error al actualizar el evento.");
                }
            }



            Console.WriteLine("\nPruebas finalizadas.");
            Console.ReadLine();
        }
    }
}
