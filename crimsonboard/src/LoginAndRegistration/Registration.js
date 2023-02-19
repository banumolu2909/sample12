import React, {useState} from 'react'
import './registration.css';
import { useNavigate } from "react-router-dom";

const Registration = () => {
    const [email, setEmail] = useState("");
    const [firstname, setFname] = useState("");
    const [lastname, setLname] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log({ firstname, lastname, email, password });
        setFname("");
        setLname("");
        setEmail("");
        setPassword("");
    };
    const gotoLoginPage = () => navigate("/");

    return (
        <div className='sprint1'>
            <div className='registration'>
                <h1>Register</h1>
                <form  onSubmit={handleSubmit}>
                    <input 
                        type='text' 
                        className='name' 
                        placeholder='First Name' 
                        id='firstname'
                        name='firstname'
                        value={firstname} 
                        required 
                        onChange={(e) => setFname(e.target.value)}
                    /><br />
                    <input 
                        type='text'
                        className='name' 
                        placeholder='Last Name' 
                        id='lastname'
                        name='lastname'
                        value={lastname} 
                        required 
                        onChange={(e) => setLname(e.target.value)} 
                    /><br />
                    <input 
                        type='email' 
                        className='mailId' 
                        placeholder='Email Address' 
                        id='email'
                        name='email'
                        value={email} 
                        required 
                        onChange={(e) => setEmail(e.target.value)}
                    /><br />
                    <input 
                        type='password' 
                        className='password' 
                        placeholder='Create Password' 
                        name='password'
                        id='password'
                        minLength={8} 
                        required 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)} 
                    /><br />
                    <input 
                        type='password' 
                        className='password' 
                        placeholder='Re-enter Password' 
                        name='password'
                        id='repassword'
                        minLength={8} 
                        required 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)} 
                    /><br />
                    <button type='button' className='logbutton'>Register</button>
                    <p>
                    Already have an account?{" "}
                    <span className='link' onClick={gotoLoginPage}>
                        Login
                    </span>
                    </p>
                    <div class="line"></div>
                    <div class="other">
                        <a href="https://code.visualstudio.com/docs/nodejs/reactjs-tutorial">Login with Gmail</a>
                    </div>
                
                </form>
            </div>
        </div>
    )
}

export default Registration;