#include "ros/ros.h"
#include "kuka/AngleValues.h"
#include <cstdlib>
#include <iostream>
#include "youbot/YouBotBase.hpp"
#include "youbot/YouBotManipulator.hpp"

using namespace youbot;
YouBotBase *initYouBotBase();
YouBotManipulator *initYouBotManipulator();

 
using namespace std;

// default youBot config installation dir
#define YOUBOT_CONFIGURATIONS_DIR "/usr/local/config/"

//начальные значения углов
float A1=0;
float A2=0;
float A3=0;
float A4=0;
float A5=0;

//main for test on kuka youbot

// int main (int argc,char **argv)
// {
//     /* configuration flags for different system configurtion (e.g. base without arm)*/
//     bool youBotHasBase = false;
//     bool youBotHasArm = false;

//     /* create handles for youBot base and manipulator (if available) */
//     YouBotBase* myYouBotBase = 0;
//     YouBotManipulator* myYouBotManipulator = 0;


//     try {
//         myYouBotBase = new YouBotBase("youbot-base", YOUBOT_CONFIGURATIONS_DIR);
//         myYouBotBase->doJointCommutation();
//         youBotHasBase = true;
//     } 

//     catch (std::exception& e) {
// 		LOG(warning) << e.what();
// 		youBotHasBase = false;
// 	}

//     try {
// 		myYouBotManipulator = new YouBotManipulator("youbot-manipulator", YOUBOT_CONFIGURATIONS_DIR);
// 		myYouBotManipulator->doJointCommutation();
// 		myYouBotManipulator->calibrateManipulator();

// 		youBotHasArm = true;
// 	} 

//     catch (std::exception& e) {
// 		LOG(warning) << e.what();
// 		youBotHasArm = false;
// 	}

//     /* Variable for the arm. */
// 	// Объявление переменных
// 	// Объекты класса для формирования командных значений углов
// 	JointAngleSetpoint desiredJointAngle;
// 	// Объект класса для измерения значений углов
// 	JointSensedAngle   sensedAngle;

//     try {

// 	    if (youBotHasArm) {
//             // Выставляем манипулятор в исходное положение
// 			desiredJointAngle.angle = A1 * radian;
// 			myYouBotManipulator->getArmJoint(1).setData(desiredJointAngle);
// 			desiredJointAngle.angle = A2 * radian;
// 			myYouBotManipulator->getArmJoint(2).setData(desiredJointAngle);
// 			desiredJointAngle.angle = A3 * radian;
// 			myYouBotManipulator->getArmJoint(3).setData(desiredJointAngle);
// 			desiredJointAngle.angle = A4 * radian;
// 			myYouBotManipulator->getArmJoint(4).setData(desiredJointAngle);
// 			desiredJointAngle.angle = A5 * radian;
// 			myYouBotManipulator->getArmJoint(5).setData(desiredJointAngle);
//             SLEEP_MILLISEC(2000);

//             //конфигурируем клиента
//             ros::init(argc,argv,"add_two_ints_client");
//             ros::NodeHandle n;
//             ros::ServiceClient client = n.serviceClient<kuka::AddTwoInts>("add_two_ints");
//             kuka::AddTwoInts srv;

//             while(true)
//             {
//                 srv.request.A4 = A4;
//                 srv.request.A5 = A5;
//                 if (client.call(srv))
//                 {
//                     A4=srv.response.A4_new;
//                     A5=srv.response.A5_new;
//                     desiredJointAngle.angle = A4 * radian;
// 			        myYouBotManipulator->getArmJoint(4).setData(desiredJointAngle);
// 			        desiredJointAngle.angle = A5* radian;
// 			        myYouBotManipulator->getArmJoint(5).setData(desiredJointAngle);
//                 }
//                 SLEEP_MILLISEC(500);

//             }


//         }
//     }

//     catch (std::exception& e) {
// 		std::cout << e.what() << std::endl;
// 		std::cout << "unhandled exception" << std::endl;
// 	}
	
// 	/* clean up */
// 	if (myYouBotBase) {
// 		delete myYouBotBase;
// 		myYouBotBase = 0;
// 	}
// 	if (myYouBotManipulator) {
// 		delete myYouBotManipulator;
// 		myYouBotManipulator = 0;
// 	}

// 	LOG(info) << "Done.";


//     return 0;


// }




//main for test without kuka youbot

int main(int argc, char **argv)
{
    ros::init(argc,argv,"kuka_arm_client");

    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<kuka::AngleValues>("kuka_arm");
    kuka::AngleValues srv;

    while (true)
    {
        srv.request.A4 = A4;
        srv.request.A5 = A5;
        cout<<"A4 is equal "<<A4<<" A5 is equal "<<A5<<endl;
        if (client.call(srv))
      {
        cout<<"A4_new is equal "<<srv.response.A4_new<<" "<<"A5_new is equal "<<srv.response.A5_new<<endl;
      }

        break;
    }
    return 0;

}