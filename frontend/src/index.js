import React from 'react';
import ReactDOM from 'react-dom/client';
import { Router, Switch, Route } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';

ReactDOM.createRoot(document.getElementById('root')).render(<App />);

