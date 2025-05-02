import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Para redirecionar após login
import api from '../services/api'; // Importando a instância do axios

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState<string | null>(null);
    const navigate = useNavigate();  // Usando o react-router-dom para redirecionar

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();

        try {
            // Enviando as credenciais para o backend Django
            const response = await api.post('/token/', { username: email, password });

            // Armazenando o token JWT no localStorage
            localStorage.setItem('token', response.data.access);

            // Redirecionando para a página principal (exemplo)
            navigate('/');
        } catch (err: any) {
            setError('Credenciais inválidas');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            <form onSubmit={handleLogin}>
                <div>
                    <label>Email</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Senha</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Entrar</button>
            </form>
        </div>
    );
};

export default Login;
