import React from "react"
import './Home.css'
import Banner from './images/banner.jpg'
import Pencil from './images/pencil.png'
import FoodStand from './images/food-stand.png'
import Bus from './images/bus.png'

function Home(){
  return(
    <div className="home">
      {/*fading banner*/}
      <img src={Banner}
      className="home__image"
      />

      {/*About Us*/}
      <div className="home__about">
        <h1>About Us</h1>
        <div className="home__description">
        <p>Parents in India still have to give children cash allowances as the transactions in schools
remain cash-based. Students normally spend too much on eating junk foods in canteens
and sometimes even on things that they shouldn’t buy. So, a system has to be developed to
enable a cashless school system which better allows parents to monitor expenditures. We at ParentPay provide a platform to the schools
allows every student to have an account for himself/herself. Parents won't have to provide money to their child as the student will have to include
every expenditure in his/her account and parents will have to pay the net amount at the end of the month to the school. Also parents will be able to see
the expenditures of every single item purchased by their child as he/she will have to give the details of the item before purchase. We have started with
a total of 3 categories but we intend to include more if the system gets the support of society.</p>
        </div>
      </div>

      <hr className="home_hr"/>

      {/*categories: transportation, food, stationary */}
      <div className="home__categories">
        <div className="home__row">
          <img src={Bus} className="home__trasportImage home_catImage" />
          <p className="home__rowPart2">Transportation is one of the categories of expenditure for students. The school will have to provide the transportation facilities and the
          expenditure on such facilities by the student will have to be added on their dashboard via our platform.</p>
        </div>

        <div className="home__row">
          <p>This is one of the major expenditure sources of students. Students tend to misuse the cash given to them by spending it on eating junk food
          from the school canteen and thus harms their own health. Our platform provides the category of Food so that the student will have to give the
          food item name before buying it thereby the parents can keep track of health of their child. Also we will have a nutrition bar for every week
          which will suggest what to eat to be healthy and fit.</p>
          <img src={FoodStand} className="home__foodImage home_catImage" />
        </div>

        <div className="home__row">
          <img src={Pencil} className="home__statImage home_catImage" />
          <p className="home__rowPart2">Stationary items are the daily requirements of students. Therefore our platform also provides a category of
          stationary items to cover overall expenditure of a student.</p>
        </div>
      </div>
    </div>
  )
}

export default Home
