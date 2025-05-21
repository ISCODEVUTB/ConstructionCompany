import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:construction_company_app/models/project.dart';

class ApiService {
  final String _baseUrl = 'https://your-backend-api.com';

  Future<List<Project>> getProjects() async {
    final response = await http.get(Uri.parse('$_baseUrl/projects'));

    if (response.statusCode == 200) {
      List jsonResponse = json.decode(response.body);
      return jsonResponse.map((item) => Project.fromJson(item)).toList();
    } else {
      throw Exception('Failed to load projects');
    }
  }
}