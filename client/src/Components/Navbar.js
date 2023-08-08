import React from 'react'
import {} from 'react-icons'

function NavBar(){
    return (
        <div className='flex justify-between items-center h-24 mx-auto px-4'>
            <img className='h-24' src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" alt="BIRTHDAZE Logo">
            </img>
            <ul className='flex'>
                <li  className='p-4 font-bold text-blue-500'>HOME</li>
                <li  className='p-4 font-bold text-blue-500'>FEATURES</li>
                <li  className='p-4 font-bold text-blue-500'>LOGIN</li>
            </ul>
        </div>
    )
}

export default NavBar;