import { useEffect, useState } from 'react'
import ProjectCard from '../components/ProjectCard'
import { getProjects } from '../services/api'

export default function Projects() {
  const [projects, setProjects] = useState([])

  useEffect(() => {
    const fetchProjects = async () => {
      const data = await getProjects()
      setProjects(data)
    }
    fetchProjects()
  }, [])

  return (
    <div className="projects-container">
      <h1>Our Projects</h1>
      <div className="projects-grid">
        {projects.map(project => (
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </div>
  )
}