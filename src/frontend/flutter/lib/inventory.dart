import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: InventoryPage()));
}

class InventoryPage extends StatelessWidget {
  const InventoryPage({super.key});

  final List<Map<String, dynamic>> items = const [
    {
      "id": "001",
      "name": "Excavadora",
      "photo": "🛠️",
      "category": "Machinery",
      "supplier": "Proveedor A",
      "location": "Bodega 1",
      "stock": 2,
      "reorder": 1,
      "unit": "pcs",
      "price": 50000.0,
      "status": "In Stock"
    },
    {
      "id": "002",
      "name": "Cemento",
      "photo": "🏗️",
      "category": "Materials",
      "supplier": "Proveedor B",
      "location": "Bodega 2",
      "stock": 0,
      "reorder": 50,
      "unit": "bags",
      "price": 0.0,
      "status": "Out of Stock"
    },
  ];

  Color _statusColor(String status) {
    switch (status) {
      case "In Stock":
        return Colors.green;
      case "Out of Stock":
        return Colors.red;
      default:
        return Colors.grey;
    }
  }

  Widget _buildSummaryRow(String category, double total) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(category),
        Text("\$${total.toStringAsFixed(2)}"),
      ],
    );
  }

  DataRow _buildRow(Map<String, dynamic> item) {
    return DataRow(cells: [
      DataCell(Text(item["id"])),
      DataCell(Text(item["name"])),
      DataCell(Text(item["photo"] ?? "")),
      DataCell(Text(item["category"])),
      DataCell(Text(item["supplier"])),
      DataCell(Text(item["location"])),
      DataCell(Text(item["stock"].toString())),
      DataCell(Text(item["reorder"].toString())),
      DataCell(Text(item["unit"])),
      DataCell(Text("\$${item["price"].toStringAsFixed(2)}")),
      DataCell(Row(
        children: [
          Icon(Icons.circle, color: _statusColor(item["status"]), size: 10),
          const SizedBox(width: 6),
          Text(item["status"]),
        ],
      )),
    ]);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xfff0f7f0),
      appBar: AppBar(
        title: const Text('Inventory Tracker'),
        backgroundColor: Colors.teal[100],
        actions: [
          TextButton(
            onPressed: () {
              // Acción para volver al dashboard
              Navigator.pop(context);
            },
            child: const Text("← Dashboard", style: TextStyle(color: Colors.black)),
          ),
        ],
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              // Barra superior tipo gráfica
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 80,
                      color: Colors.lightBlue[100],
                      child: const Center(child: Text("Machinery")),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Container(
                      height: 80,
                      color: Colors.blue[800],
                      child: const Center(
                          child: Text("Materials",
                              style: TextStyle(color: Colors.white))),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              // Tabla
              Expanded(
                child: SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: SizedBox(
                    width: 1200, // fuerza a que se expanda más
                    child: SingleChildScrollView(
                      scrollDirection: Axis.vertical,
                      child: DataTable(
                        columnSpacing: 16,
                        columns: const [
                          DataColumn(label: Text("Item ID")),
                          DataColumn(label: Text("Item Name")),
                          DataColumn(label: Text("SKU Photo")),
                          DataColumn(label: Text("Category")),
                          DataColumn(label: Text("Supplier")),
                          DataColumn(label: Text("Location")),
                          DataColumn(label: Text("Stock Level")),
                          DataColumn(label: Text("Reorder Level")),
                          DataColumn(label: Text("Unit")),
                          DataColumn(label: Text("Total Inventory Price")),
                          DataColumn(label: Text("Stock Status")),
                        ],
                        rows: items.map(_buildRow).toList(),
                      ),
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              // Resumen
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text("Summary", style: TextStyle(fontWeight: FontWeight.bold)),
                        const SizedBox(height: 4),
                        _buildSummaryRow("Machinery", 50000),
                        _buildSummaryRow("Materials", 0),
                      ]),
                  const Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text("\$50000.00"),
                      Text("\$0.00"),
                    ],
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
