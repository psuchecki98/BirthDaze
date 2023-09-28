import React, { useState, useEffect } from 'react'
// import { NavLink } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
import UserNavBar from './UserNavBar';
import CardBirthday from './CardBirthday';

function UserBirthdays() {
    const [birthdays, setBirthdays] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/birthdays')
        .then((resp) => resp.json())
        .then((data) => {
            setBirthdays(data)
        })
    }, [])

    const birthdaysInfo = birthdays?.map((birthday) => {
        return <CardBirthday key={birthday.id} birthday={birthday} />
    })

    return (
        <>
            <div className='border-y-2'>
                <UserNavBar />
            </div>
            
            <div className="grid grid-cols-2 gap-4 h-screen bg-white pd-5 pl-[10%]">
                {birthdaysInfo}
            </div>
        </>
        
    );
}

export default UserBirthdays;