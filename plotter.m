%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MATLAB plotter based on example.m
% by S. Foteinopoulou Jul. 20, 2006
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all;

%provide x and y dimensions of the domain to be plotted
xdim=201;
ydim=201;

%ask matlab to create a figure

figure;

%Read data from your experimental or numerical data file

field=load('Emu-1_eps100_data8.txt');

%Convert data file to matrices that can be read from matlab

xx=field(:,1); %first column of data represents x
yy=field(:,2); %second column of data represents y
zz=field(:,3); %third column represnts value of field, intensity e.t.c.

for i=1:xdim
    x1p(i)=xx((i-1)*ydim+1); 
    for j=1:ydim
      z1p(j,i)=(zz((i-1)*ydim+j));
    end
end 


for k=1:ydim
  y1p(k)=yy(k);
end

%!!!!!!!! CAREFUL !!!!!!!!!!!
% this script applies only to input files where
% for each x, y varies and not vice versa
  grid off; %don't put any grid lines
  axis on; %show x and y axis --off don't show
axis equal; % keep scaling as the real scaling- don't compress or
            %expand axis
%--------------------
% 2D surface plots
%-------------------

pcolor(x1p,y1p,z1p);

colorbar(); %put a colorbar showing mapping 
                  %between colors and values

title("A map of the Electric Field Strength: m=-5 to 5 eps=100 mu=-1 wa/c=0.08"); % 
xlabel("x");
ylabel("y"); 

shading interp;   %gives usually best view interpolates between grids
colormap('jet');  %choose the colormap other options hsv,cool,hot e.t.c.

%Plots the Cylinder Cross Section For Comparison
hold;
t = [0:0.1:2*pi];
x = cos(t);
y = sin(t);
plot(x, y,'.');
%%%----------------------

print -djpeg 'insert jpeg name' #low_up_peak (01 =0.1)_eps


