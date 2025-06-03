import 'package:http/http.dart' as http;
import '../config.dart';
import 'dart:convert';

class ApiService {
  Future<http.Response> fetchUsers() async {
    final response = await http.get(Uri.parse('$backendUrl/users/'));
    return response;
  }

  Future<http.Response> registerUser(
      String username, String email, String password, String rol) async {
    final response = await http.post(
      Uri.parse('$backendUrl/users/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'nombre': username,
        'email': email,
        'password': password,
        'rol': rol,
      }),
    );
    return response;
  }
}