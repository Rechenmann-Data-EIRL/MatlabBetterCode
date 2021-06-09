function nested_function(array)
    squared_array = zeros(length(array),1)
    for index = 1:length(array)
        squared_array(index) = squared(index)
    end

    function square = squared(value)
        square = value * value;
    end

end