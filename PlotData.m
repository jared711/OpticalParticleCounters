clc
close all
clear all

DataLog = xlsread('J:\Research\Data\CalibrationTank\OpticalParticleCounters\DATA\GoodData\TestLog.csv')
% Pretest1 = xlsread('J:\Research\Data\CalibrationTank\Pretest1(FromAmbientToZero)_1-24-18.csv');
% Test1 = xlsread('J:\Research\Data\CalibrationTank\TEST1(LB5)_1-25-18.csv');
% Test2 = xlsread('J:\Research\Data\CalibrationTank\TEST2(LB30)_1-25-18.csv');
% Test3 = xlsread('J:\Research\Data\CalibrationTank\TEST3(De-ionizedWater)_1-25-18.csv');
% Test4 = xlsread('J:\Research\Data\CalibrationTank\TEST4(LB5)_1-26-18.csv');
% Test5 = xlsread('J:\Research\Data\CalibrationTank\TEST5(LB30)_1-26-18.csv');
% Test6 = xlsread('J:\Research\Data\CalibrationTank\TEST6(DistilledWater)_1-26-18.csv');
% Test7 = xlsread('J:\Research\Data\CalibrationTank\TEST7(LB5)_1-26-18.csv');
% Test8 = xlsread('J:\Research\Data\CalibrationTank\TEST8(LB30)_1-26-18.csv');
% Test9 = xlsread('J:\Research\Data\CalibrationTank\TEST9(DistilledWater)_1-26-18MISREAD.csv');
% Test10 = xlsread('J:\Research\Data\CalibrationTank\TEST10.csv');
% Test11 = xlsread('J:\Research\Data\CalibrationTank\TEST11.csv');
% Test12 = xlsread('J:\Research\Data\CalibrationTank\TEST12.csv');
% % 
% % figure
% % plot(Pretest1(:,2),Pretest1(:,4))
% % title("Pretest1")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test1(:,2),Test1(:,4))
% % title("Test1")
% % title("1 ?L of solution in 1 mL of water w/ diffusion dryer")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test2(:,2),Test2(:,4))
% % title("Test2")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test3(:,2),Test3(:,4))
% % title("Test3")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test4(:,2),Test4(:,4))
% % title("Test4")
% % title("1 ?L of solution in 1 mL of water w/out diffusion dryer")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test5(:,2),Test5(:,4))
% % title("Test5")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test6(:,2),Test6(:,4))
% % title("Test6")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test7(:,2),Test7(:,4))
% % title("Test7")
% % title("1 ?L of solution in 8 mL of water w/out diffusion dryer")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test8(:,2),Test8(:,4))
% % title("Test8")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test9(:,2),Test9(:,4))
% % title("Test9")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test10(:,2),Test10(:,4))
% % title("Test10")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% % figure
% % plot(Test11(:,2),Test11(:,4))
% % title("Test11")
% % xlabel("Time [s]")
% % ylabel("PM2.5 [?g/m^3]")
% figure
% hold on
% plot(Test12(:,2),Test12(:,3))
% plot(Test12(:,2),Test12(:,4))
% plot(Test12(:,2),Test12(:,5))
% title("Test12")
% xlabel("Time [s]")
% ylabel("PM2.5 [?g/m^3]")
% legend("PM_{10}","PM_{2.5}","PM_{1}")

% err = zeros(1,length(Test12));
% % n = 1000;
% % i = n;
% % while(i < length(Test12)/n)
% %     err(i) = Test12(i,4);
% %     i = i + n;
% % end%Test12(:,4) * 0.01;
% errorbar(Test12(:,2),Test12(:,4),err)