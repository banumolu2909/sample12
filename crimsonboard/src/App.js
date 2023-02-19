import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './LoginAndRegistration/Login'
import Registration from './LoginAndRegistration/Registration';

function App() {
  
    return (
        <BrowserRouter>
        <Routes>
          <Route path='/' element={<Login />} />
          <Route path='/register' element={<Registration />} />
        </Routes>
      </BrowserRouter>
      
    );
}
export default App;

