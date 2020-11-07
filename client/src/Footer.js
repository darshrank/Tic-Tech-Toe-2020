import React from "react"
import './Footer.css'
import { AiOutlineFacebook,AiOutlineMail,AiOutlineInstagram } from 'react-icons/ai';
import { FaGithub } from 'react-icons/fa';
import {FiTwitter} from 'react-icons/fi';

function Footer(){
    return (
      <div className="footer">
        <div className="contacts">
          <h1>Contact Us</h1>
          <li>Darsh - 9228210710</li>
          <li>Sattu - 8128984425</li>
          <li>Himil - 7078289526</li>
          <li>Priyansh - 8511641211</li>
        </div>
        <div className="logos">
          <AiOutlineFacebook className="logo" />
          <a href="https://github.com/darshrank/Tic-Tech-Toe-2020" target="_blank"><FaGithub className="logo" /></a>
          <FiTwitter className="logo"/>
          <AiOutlineMail className="logo"/>
          <AiOutlineInstagram className="logo"/>
        </div>
      </div>
    )
}

export default Footer
