import 'package:flutter/material.dart';

class ProjectsPage extends StatelessWidget {
  final List<Map<String, dynamic>> projects = [
    {
      "name": "Edificio Central",
      "status": "En progreso",
      "startDate": "2024-06-01"
    },
    {
      "name": "Puente Norte",
      "status": "Retrasado",
      "startDate": "2024-05-15"
    },
    {
      "name": "Parque Industrial",
      "status": "Completado",
      "startDate": "2023-12-10"
    },
  ];

  ProjectsPage({super.key});

  Color _statusColor(String status) {
    switch (status) {
      case "En progreso":
        return Colors.blue;
      case "Retrasado":
        return Colors.red;
      case "Completado":
        return Colors.green;
      default:
        return Colors.grey;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Proyectos"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Card(
          elevation: 2,
          child: DataTable(
            columns: const [
              DataColumn(label: Text("Nombre")),
              DataColumn(label: Text("Estado")),
              DataColumn(label: Text("Fecha de inicio")),
            ],
            rows: projects
                .map(
                  (project) => DataRow(
                    cells: [
                      DataCell(Text(project["name"])),
                      DataCell(Row(
                        children: [
                          Icon(Icons.circle, color: _statusColor(project["status"]), size: 12),
                          const SizedBox(width: 8),
                          Text(project["status"]),
                        ],
                      )),
                      DataCell(Text(project["startDate"])),
                    ],
                  ),
                )
                .toList(),
          ),
        ),
      ),
    );
  }
}