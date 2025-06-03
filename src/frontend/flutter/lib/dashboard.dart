import 'package:flutter/material.dart';
import 'inventory.dart';
import 'projects.dart';

class DashboardPage extends StatelessWidget {
  const DashboardPage({Key? key}) : super(key: key);

  Widget _dashboardCard(String title, String subtitle, {Widget? child}) {
    return Container(
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.grey[200],
        borderRadius: BorderRadius.circular(24),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 20)),
          const SizedBox(height: 8),
          Text(subtitle, style: const TextStyle(fontSize: 16, color: Colors.black54)),
          if (child != null) ...[
            const SizedBox(height: 16),
            child,
          ]
        ],
      ),
    );
  }

  Widget _sideMenu(BuildContext context) {
    return Container(
      width: 200,
      color: Colors.black87,
      child: Column(
        children: [
          const SizedBox(height: 40),
          _menuButton(context, "Dashboard", () {}),
          _menuButton(context, "Inventory", () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => InventoryPage()),
            );
          }),
          _menuButton(context, "Projects", () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ProjectsPage()),
            );
          }),
          // Agrega más botones aquí si lo deseas
        ],
      ),
    );
  }

  Widget _menuButton(BuildContext context, String text, VoidCallback onPressed) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.white,
          foregroundColor: Colors.black87,
          minimumSize: const Size.fromHeight(40),
        ),
        child: Align(
          alignment: Alignment.centerLeft,
          child: Text(text),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      body: Row(
        children: [
          _sideMenu(context),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(32),
              child: SingleChildScrollView(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Top bar
                    const Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text("Dashboarb", style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
                        Row(
                          children: [
                            Icon(Icons.notifications_none, size: 32),
                            SizedBox(width: 16),
                            CircleAvatar(child: Icon(Icons.person)),
                          ],
                        ),
                      ],
                    ),
                    const SizedBox(height: 32),
                    // Top cards
                    Row(
                      children: [
                        Expanded(child: _dashboardCard("Projects", "NUMBER OF PROJECTS\nActive")),
                        const SizedBox(width: 24),
                        Expanded(child: _dashboardCard("Inventory Items", "NUMBER OF ITEMS\nAvailable")),
                        const SizedBox(width: 24),
                        Expanded(child: _dashboardCard("Costs", "\$ \nCurrent")),
                      ],
                    ),
                    const SizedBox(height: 24),
                    // Middle cards
                    Row(
                      children: [
                        Expanded(
                          flex: 2,
                          child: _dashboardCard(
                            "Equipment Availability",
                            "",
                            child: Container(
                              height: 120,
                              color: Colors.grey[400], // Placeholder for chart
                            ),
                          ),
                        ),
                        const SizedBox(width: 24),
                        Expanded(
                          flex: 2,
                          child: _dashboardCard(
                            "Project Progress",
                            "",
                            child: Container(
                              height: 120,
                              color: Colors.grey[400], // Placeholder for chart
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),
                    // Bottom cards
                    Row(
                      children: [
                        Expanded(
                          child: _dashboardCard(
                            "Projects",
                            "Project Name    IN PROGRESS\nProject Name 2  DELAYED",
                          ),
                        ),
                        const SizedBox(width: 24),
                        Expanded(
                          child: _dashboardCard(
                            "Inventory",
                            "Material      AVAILABLE\nEquipment     UNAVAILABLE",
                          ),
                        ),
                        const SizedBox(width: 24),
                        Expanded(
                          child: _dashboardCard(
                            "Purchases",
                            "Supplies   STATUS\nMaterial   STATUS",
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}