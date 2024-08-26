/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (!obj) return false;
    if (typeof obj !== 'object') return obj;

    if (Array.isArray(obj)){
        return obj
            .map(item => compactObject(item)) // Recursively compact each item
            .filter(item => item !== undefined && item !== null && item !== false && item !== 0 && item !== ''); 
    }
   
    // If the object is a plain object
    let compactObj = {};
    for (const key in obj) {
        const value = compactObject(obj[key]);
        
        // Only include truthy values in the resulting object
        if (value) {
            compactObj[key] = value;
        }
    }
    
    return compactObj;

};