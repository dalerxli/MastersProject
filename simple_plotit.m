
load CS_mun1_epsn100_1.txt

x=CS_mun1_epsn100_1(:,1);  %% extracts column 'x' from matrix 'data'   
y=CS_mun1_epsn100_1(:,2);  %% extracts column 'y' from matrix 'data'


plot(x,y,'bs-','MarkerSize',5,'LineWidth',1); 
set(gca,'LineWidth',4,'FontSize',20) 
set(gca,'position',[0.12,0.2,0.85,0.7]);

%axis([0 10 0 10]); %% specifies the axis limits
title('Scattering cross section eps=-100, mu=-1');
xlabel('wa/c','FontName','Times','FontSize',12); %% xLabel together with font attributes
ylabel('Scattering Cross Section','FontName','Times','FontSize',12); %% yLabel 

print('SCS_mu-1_eps-100_1.jpg','-djpg');
                           
