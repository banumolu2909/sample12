import React, { useState } from "react";
import './login.css';
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log({ email, password });
        setPassword("");
        setEmail("");
    };

    const gotoSignUpPage = () => navigate("/register");

    return (
        <div className='sprint1'>
            <div className='login'>
                <h1>Login</h1>
                <form  onSubmit={handleSubmit}>
                    <input 
                        type='text' 
                        className='mailId'
                        id='email'
                        name='email'
                        placeholder='Email Address' 
                        value={email}
                        required
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <input 
                        type='password' 
                        className='password' 
                        placeholder='Enter Password' 
                        name='password'
                        id='password'
                        minLength={8}
                        required
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    /><br />
                    <a href='https://code.visualstudio.com'>Forgot Password?</a><br />
                    <button type='button' className='logbutton'>Login</button>
                    <p>
                    Don't have an account?{" "}
                    <span className='link' onClick={gotoSignUpPage}>
                        Sign up
                    </span>
                </p>
                <hr
                    style={{
                    background: "#47B5FF",
                    height: "2px",
                    border: "none",
                    }}
                />
                <div class="other"></div>
                <button type='button' className='googlebutton'>Google Login</button>
                </form>
            </div>
        </div>
    );
};

export default Login;