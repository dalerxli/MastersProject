function peak_finder

load CS_mun1_epsn100_1.txt

x=CS_mun1_epsn100_1(:,1);  %% extracts column 'x' from matrix 'data'   
y=CS_mun1_epsn100_1(:,2);  %% extracts column 'y' from matrix 'data'

x=transpose(x);
y=transpose(y);

[pks,loc]=findpeaks(y);

output=[loc',pks']

save peaks_mun1_epsn1.txt output 

endfunction

%Just like findpeaks() in matlab
function [pks,loc]=findpeaks(y)

tot_pks=columns(y)
pks=[]
loc=[]


for n=2:(tot_pks-1)

	lower=y(n-1);
	upper=y(n+1);
	current=y(n);
	

	if current>lower & current>upper
	pks=[pks current];
	loc=[loc n*0.0001];
	end
	
	

end

endfunction




