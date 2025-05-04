
import api, { apiPublic } from './api';

interface LoginResponse {
  access: string;
  refresh: string;
}

export const login = async (username: string, password: string): Promise<LoginResponse> => {
  const response = await api.post<LoginResponse>('/auth/token/', { username, password });
  return response.data;
};

export const register = async (data: {
  username: string;
  email?: string;
  bio?: string;
  password: string;
}) => {
  const response = await apiPublic.post('/auth/register/', data);
  return response.data;
};
