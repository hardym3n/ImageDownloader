<template>
    <div class="image_item_wrapper">
        <img v-bind:src="data.url" alt="" width="75" height="75">
        <div class="item__info">
            <div class="text__url"><a v-bind:href="data.url">{{ data.url }}</a></div>
            <div class="text__ext"><span>{{ data.ext }}</span> <span v-if="data.width != null">{{ data.width }}x{{ data.height }}</span></div>
            
            <div class=""></div>
        </div>
        <div class="item__action__wrapper">
            <div>
                <a target="_blank" :href="data.url"  class="button__download"></a>
            </div>
            <div class="text__size"><span>{{ data.size }}</span></div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ImageItem",
    props: {
        data: Object
    },
}
</script>

<style lang="scss">
.image_item_wrapper{
    border-radius: 10px;
    box-shadow: 5px 15px 15px rgba($color: #000000, $alpha: .03);
    padding: 15px 15px;
    border: 1px solid #eee;
    margin-top: 15px;
    display: flex;
    width: 100%;
    img{
        border-radius: 10px;
        object-fit: cover;
    }
}
.text__url{
    font-size: 12px;
}
.text__size{
    font-size: 12px;
}
.item__info{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    padding: 0px 15px;
}
.button__download{
    width: 50px;
    height: 50px;
    display: block;
    background: url('../assets/down-arrow.svg');
    background-size: 25px;
    background-repeat: no-repeat;
    background-position: center;
}
.item__action__wrapper{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
</style>