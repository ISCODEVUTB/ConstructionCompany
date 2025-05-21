export default function ProjectCard({ project }) {
  return (
    <div className="project-card">
      <h3>{project.name}</h3>
      <p>Location: {project.location}</p>
      <p>Status: {project.status}</p>
      <p>Budget: ${project.budget.toLocaleString()}</p>
    </div>
  )
}