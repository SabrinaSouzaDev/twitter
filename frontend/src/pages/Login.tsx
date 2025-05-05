import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../styles/login.css';
import { login } from '../services/authService';


const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState<string | null>(null);
    const navigate = useNavigate();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const { access, refresh } = await login(username, password);
            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
            const token_obtain_pair = `Bearer ${access}`;
            navigate(`/swagger/?token=${encodeURIComponent(token_obtain_pair)}`);
        } catch {
            setError('Usuário ou senha inválidos');
        }
    };


    return (
        <div className="login-container">
            <div className="login-card">
                <h1 className="login-logo">MINI-TWITTER</h1>
                <h2 className="login-title">Entrar na sua conta</h2>

                {error && <div className="login-error">{error}</div>}

                <form onSubmit={handleLogin} className="login-form">
                    <div className="login-form-group">
                        <label className="login-label">Usuário</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="login-input"
                            required
                        />
                    </div>
                    <div className="login-form-group">
                        <label className="login-label">Senha</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="login-input"
                            required
                        />
                    </div>
                    <button type="submit" className="login-button">Login</button>
                </form>

                <p className="login-signup-text">
                    Não tem uma conta?{' '}
                    <Link to="/Register" className="login-signup-link">
                        Criar nova conta
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default Login;
