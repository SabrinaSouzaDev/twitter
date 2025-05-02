import axios from 'axios';

// Criação da instância axios
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api', // Usando a variável de ambiente do CRA
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para adicionar o token JWT às requisições
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');  // Recupera o token do localStorage
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;  // Adiciona o token ao cabeçalho
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
