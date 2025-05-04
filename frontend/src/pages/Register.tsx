import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../styles/register.css';
import { register } from '../services/authService';

const Register = () => {
    const [form, setForm] = useState({
        username: '',
        email: '',
        bio: '',
        password: '',
        confirmPassword: '',
    });
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<string | null>(null);
    const navigate = useNavigate();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleRegister = async (e: React.FormEvent) => {
        e.preventDefault();
        if (form.password !== form.confirmPassword) {
            return setError('As senhas não coincidem.');
        }

        try {
            await register({
                username: form.username,
                email: form.email || undefined,
                bio: form.bio || undefined,
                password: form.password,
            });
            setSuccess('Conta criada com sucesso!');
            setTimeout(() => navigate('/'), 1500);
        } catch {
            setError('Erro ao registrar. Verifique os dados.');
        }
    };

    return (
        <div className="register-container">
            <div className="register-card">
                <h1 className="register-logo">MINI-TWITTER</h1>
                <h2 className="register-title">Criar Conta</h2>

                {error && <div className="register-error">{error}</div>}
                {success && <div className="register-success">{success}</div>}

                <form onSubmit={handleRegister} className="register-form">
                    <div className="register-form-group">
                        <label>Usuário*</label>
                        <input
                            type="text"
                            name="username"
                            value={form.username}
                            onChange={handleChange}
                            required
                            pattern="^[\w.@+-]+$"
                            maxLength={150}
                            minLength={1}
                            className="register-input"
                        />
                    </div>

                    <div className="register-form-group">
                        <label>Email</label>
                        <input
                            type="email"
                            name="email"
                            value={form.email}
                            onChange={handleChange}
                            className="register-input"
                            maxLength={254}
                        />
                    </div>

                    <div className="register-form-group">
                        <label>Bio</label>
                        <textarea
                            name="bio"
                            value={form.bio}
                            onChange={handleChange}
                            className="register-input"
                            rows={2}
                        />
                    </div>

                    <div className="register-form-group">
                        <label>Senha*</label>
                        <input
                            type="password"
                            name="password"
                            value={form.password}
                            onChange={handleChange}
                            required
                            className="register-input"
                            minLength={1}
                        />
                    </div>

                    <div className="register-form-group">
                        <label>Confirmar Senha*</label>
                        <input
                            type="password"
                            name="confirmPassword"
                            value={form.confirmPassword}
                            onChange={handleChange}
                            required
                            className="register-input"
                            minLength={1}
                        />
                    </div>

                    <button type="submit" className="register-button">Registrar</button>
                </form>

                <p className="register-login-text">
                    Já tem uma conta?{' '}
                    <Link to="/Login" className="register-login-link">
                        Fazer login
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default Register;
