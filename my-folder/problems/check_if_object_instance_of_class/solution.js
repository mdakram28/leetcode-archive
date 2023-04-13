/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj==null || classFunction==null || !classFunction.call) return false;
    return classFunction === Object || obj.__proto__ === classFunction.prototype || obj instanceof classFunction
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */