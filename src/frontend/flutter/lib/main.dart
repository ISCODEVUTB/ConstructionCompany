import 'package:flutter/material.dart';
import 'services/api_services.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Prestige Company',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'Arial',
        primarySwatch: Colors.blue,
      ),
      home: const LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final apiService = ApiService();
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  bool _isLoading = false;

  Future<void> _registerUser() async {
    setState(() => _isLoading = true);
    final response = await apiService.registerUser(
      _usernameController.text,
      _emailController.text,
      _passwordController.text,
    );
    setState(() => _isLoading = false);

    if (response.statusCode == 201) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Usuario registrado correctamente')),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error: ${response.body}')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      body: Stack(
        children: [
          SizedBox.expand(
            child: Image.asset(
              'assets/bg.jpg',
              fit: BoxFit.cover,
            ),
          ),
          Container(
            color: Colors.black.withAlpha((0.65 * 255).toInt()),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 60, vertical: 30),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Top bar
                  const Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          _NavButton(text: 'Home'),
                          SizedBox(width: 30),
                          _NavButton(text: 'About Us'),
                          SizedBox(width: 30),
                          _NavButton(text: 'Help'),
                        ],
                      ),
                      Row(
                        children: [
                          Text(
                            'Prestige Company',
                            style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              fontSize: 22,
                            ),
                          ),
                          SizedBox(width: 10),
                          Icon(Icons.construction, color: Colors.white, size: 28),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 40),
                  Expanded(
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // Contact info (bottom left)
                        const Expanded(
                          flex: 1,
                          child: Align(
                            alignment: Alignment.bottomLeft,
                            child: Padding(
                              padding: EdgeInsets.only(bottom: 30),
                              child: SingleChildScrollView(
                                child: Row(
                                  crossAxisAlignment: CrossAxisAlignment.end,
                                  children: [
                                    _ContactInfo(
                                      icon: Icons.phone,
                                      label: 'Phone',
                                      value: '+123-456-7890',
                                    ),
                                    SizedBox(width: 30),
                                    _ContactInfo(
                                      icon: Icons.language,
                                      label: 'Website',
                                      value: 'www.reallygreatsite.com',
                                    ),
                                    SizedBox(width: 30),
                                    _ContactInfo(
                                      icon: Icons.email,
                                      label: 'E-Mail',
                                      value: 'hello@reallygreatsite.com',
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                        // Login Card (right)
                        Expanded(
                          flex: 2,
                          child: Align(
                            alignment: Alignment.centerRight,
                            child: Container(
                              width: 430,
                              padding: const EdgeInsets.symmetric(horizontal: 36, vertical: 36),
                              decoration: BoxDecoration(
                                color: Colors.white.withAlpha((0.92 * 255).toInt()),
                                borderRadius: BorderRadius.circular(32),
                                boxShadow: [
                                  BoxShadow(
                                    color: Colors.black.withAlpha((0.18 * 255).toInt()),
                                    blurRadius: 24,
                                    offset: const Offset(0, 8),
                                  ),
                                ],
                              ),
                              child: SingleChildScrollView(
                                child: Form(
                                  key: _formKey,
                                  child: Column(
                                    mainAxisSize: MainAxisSize.min,
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      const Center(
                                        child: Text(
                                          'LOGIN TO YOUR\nACCOUNT',
                                          textAlign: TextAlign.center,
                                          style: TextStyle(
                                            fontSize: 28,
                                            fontWeight: FontWeight.w900,
                                            color: Color(0xFF232A3E),
                                            letterSpacing: 1.2,
                                          ),
                                        ),
                                      ),
                                      const SizedBox(height: 32),
                                      const _Label('Username  :'),
                                      const SizedBox(height: 8),
                                      _RoundedInput(
                                        hint: 'Enter your username',
                                        controller: _usernameController,
                                      ),
                                      const SizedBox(height: 18),
                                      const _Label('Email Address :'),
                                      const SizedBox(height: 8),
                                      _RoundedInput(
                                        hint: 'Enter your email',
                                        controller: _emailController,
                                      ),
                                      const SizedBox(height: 18),
                                      const _Label('Password :'),
                                      const SizedBox(height: 8),
                                      _RoundedInput(
                                        hint: 'Enter your password',
                                        obscure: true,
                                        controller: _passwordController,
                                      ),
                                      const SizedBox(height: 32),
                                      Row(
                                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                        children: [
                                          Column(
                                            crossAxisAlignment: CrossAxisAlignment.start,
                                            children: [
                                              const Text(
                                                "Don't have an account?",
                                                style: TextStyle(
                                                  fontSize: 13,
                                                  color: Color(0xFF232A3E),
                                                ),
                                              ),
                                              TextButton(
                                                onPressed: () {},
                                                style: TextButton.styleFrom(
                                                  padding: EdgeInsets.zero,
                                                  minimumSize: const Size(0, 0),
                                                  tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                                                ),
                                                child: const Text(
                                                  'Sign Up now',
                                                  style: TextStyle(
                                                    color: Colors.blue,
                                                    fontWeight: FontWeight.bold,
                                                    fontSize: 13,
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                          SizedBox(
                                            height: 48,
                                            child: ElevatedButton(
                                              onPressed: _isLoading
                                                  ? null
                                                  : () {
                                                      if (_formKey.currentState!.validate()) {
                                                        _registerUser();
                                                      }
                                                    },
                                              style: ElevatedButton.styleFrom(
                                                backgroundColor: const Color(0xFF232A3E),
                                                shape: RoundedRectangleBorder(
                                                  borderRadius: BorderRadius.circular(24),
                                                ),
                                                padding: const EdgeInsets.symmetric(horizontal: 36),
                                              ),
                                              child: _isLoading
                                                  ? const SizedBox(
                                                      width: 24,
                                                      height: 24,
                                                      child: CircularProgressIndicator(
                                                        color: Colors.white,
                                                        strokeWidth: 2,
                                                      ),
                                                    )
                                                  : const Text(
                                                      'LOGIN',
                                                      style: TextStyle(
                                                        fontWeight: FontWeight.bold,
                                                        fontSize: 18,
                                                        letterSpacing: 1.2,
                                                      ),
                                                    ),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

// Widgets auxiliares

class _NavButton extends StatelessWidget {
  final String text;
  const _NavButton({required this.text});
  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: () {},
      style: TextButton.styleFrom(
        foregroundColor: Colors.white,
        textStyle: const TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
      ),
      child: Text(text),
    );
  }
}

class _ContactInfo extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;
  const _ContactInfo({required this.icon, required this.label, required this.value});
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(icon, color: Colors.white, size: 22),
        const SizedBox(width: 8),
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(label, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 13)),
            Text(value, style: const TextStyle(color: Colors.white, fontSize: 13)),
          ],
        ),
      ],
    );
  }
}

class _Label extends StatelessWidget {
  final String text;
  const _Label(this.text);
  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: const TextStyle(
        color: Color(0xFF232A3E),
        fontWeight: FontWeight.bold,
        fontSize: 15,
      ),
    );
  }
}

class _RoundedInput extends StatelessWidget {
  final String hint;
  final bool obscure;
  final TextEditingController? controller;
  const _RoundedInput({required this.hint, this.obscure = false, this.controller});
  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      obscureText: obscure,
      validator: (value) => value == null || value.isEmpty ? 'Campo requerido' : null,
      decoration: InputDecoration(
        hintText: hint,
        filled: true,
        fillColor: const Color(0xFFF5F7FA),
        contentPadding: const EdgeInsets.symmetric(vertical: 14, horizontal: 18),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(24),
          borderSide: BorderSide.none,
        ),
      ),
    );
  }
}