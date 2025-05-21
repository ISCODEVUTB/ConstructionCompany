import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
})

export const getProjects = async () => {
  const response = await api.get('/projects')
  return response.data
}

export const login = async (credentials) => {
  const response = await api.post('/auth/login', credentials)
  return response.data
}