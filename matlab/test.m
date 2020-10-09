function a = convs(varargin )
a=1;
for i = 1:nargin 
    a = conv(a, varargin{1});
end

