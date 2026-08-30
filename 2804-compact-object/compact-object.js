var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        const result = [];

        for (const item of obj) {
            if (item) {
                result.push(
                    typeof item === "object"
                        ? compactObject(item)
                        : item
                );
            }
        }

        return result;
    }

    const result = {};

    for (const key in obj) {
        const value = obj[key];

        if (value) {
            result[key] =
                typeof value === "object"
                    ? compactObject(value)
                    : value;
        }
    }

    return result;
};