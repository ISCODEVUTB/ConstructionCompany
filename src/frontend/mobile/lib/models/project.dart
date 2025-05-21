class Project {
  final String id;
  final String name;
  final String location;
  final double budget;
  final String status;

  Project({
    required this.id,
    required this.name,
    required this.location,
    required this.budget,
    required this.status,
  });

  factory Project.fromJson(Map<String, dynamic> json) {
    return Project(
      id: json['id'],
      name: json['name'],
      location: json['location'],
      budget: json['budget'].toDouble(),
      status: json['status'],
    );
  }
}