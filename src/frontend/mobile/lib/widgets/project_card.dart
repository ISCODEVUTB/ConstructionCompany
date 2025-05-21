import 'package:flutter/material.dart';
import 'package:construction_company_app/models/project.dart';

class ProjectCard extends StatelessWidget {
  final Project project;

  const ProjectCard({super.key, required this.project});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.all(8.0),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              project.name,
              style: Theme.of(context).textTheme.headline6,
            ),
            const SizedBox(height: 8),
            Text('Location: ${project.location}'),
            Text('Status: ${project.status}'),
            Text('Budget: \$${project.budget.toStringAsFixed(2)}'),
          ],
        ),
      ),
    );
  }
}