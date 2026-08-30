class EventEmitter {
    constructor() {
        this.events = {};
    }

    subscribe(event, cb) {
        if (!this.events[event]) {
            this.events[event] = [];
        }

        this.events[event].push(cb);

        return {
            unsubscribe: () => {
                const index = this.events[event].indexOf(cb);

                this.events[event].splice(index, 1);
            }
        };
    }

    emit(event, args = []) {
        if (!this.events[event]) {
            return [];
        }

        const result = [];

        for (const cb of this.events[event]) {
            result.push(cb(...args));
        }

        return result;
    }
}