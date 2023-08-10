import React, { useState } from 'react';
import { Route, Routes } from 'react-router-dom';

import HomePage from './Components/HomePage';
import SignIn from './Components/SignIn';
import SignUp from './Components/Signup';
import UserHomePage from './Components/UserHomePage';
import UserBirthdays from './Components/UserBirthdays';
import UserFriends from './Components/UserFriends';

import UserContext from './Context/UserContext';

function App() {

  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <div>
        <Routes>
          <Route path='/' element={<HomePage />}/>
          <Route path='/signin' element={<SignIn />}/>
          <Route path='/signup' element={<SignUp />}/>
          <Route path='/user' element={<UserHomePage />}/>
          <Route path='/birthdays' element={<UserBirthdays />}/>
          <Route path='/friends' element={<UserFriends />}/>
        </Routes>
      </div>
    </UserContext.Provider>
  );
}

export default App;
