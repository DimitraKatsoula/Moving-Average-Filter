%%%%% Moving-Average Filter
% y(n)=(1/windowSize)*[x(n)+x(n-1)+...+x(n-(windowSize-1))]
t = linspace(-pi,pi,100);    % size(t) = 1x100
rng default  % initialize random number generator,
             % to make values random
x = sin(t) + 0.25*rand(size(t)); % adding noise |1+|
windowSize = 5;
w=rand(size(t));
b = (1/windowSize)*ones(1,windowSize); % [1 1 1 1 1]
a =1;
y = filter(b,a,x);
plot(t,x)
hold on
plot(t,y)
legend('Input Data with noise: x','Filtered Data without noise: y')
% Equation that filter function uses (equation of differences):
% a0*y(n)=-sum(k=1 to N)(ak*y(n-k))+sum(m=0 to M)(bm*x(n-m)),
% with a0=1,ak=a,bm=b.
